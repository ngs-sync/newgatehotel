-- Table master_departments
CREATE TABLE master_departments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR NOT NULL,
    department_name VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    UNIQUE (tenant_id, department_name)
);

-- Table master_articles
CREATE TABLE master_articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR NOT NULL,
    department_id UUID REFERENCES master_departments(id),
    article_code VARCHAR NOT NULL,
    article_name VARCHAR NOT NULL,
    type VARCHAR NOT NULL,
    is_taxable BOOLEAN DEFAULT false,
    is_service_chargeable BOOLEAN DEFAULT false,
    gl_code VARCHAR,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    UNIQUE (tenant_id, article_code),
    CHECK (type IN ('SALES', 'PAYMENT')),
    CHECK (NOT (type = 'PAYMENT' AND (is_taxable = true OR is_service_chargeable = true)))
);

-- Enable RLS
ALTER TABLE master_departments ENABLE ROW LEVEL SECURITY;
ALTER TABLE master_articles ENABLE ROW LEVEL SECURITY;

-- Add RLS Policies (allowing 'authenticated' access as per task)
CREATE POLICY "Enable all for authenticated" ON master_departments FOR ALL TO authenticated USING (true) WITH CHECK (true);
CREATE POLICY "Enable all for authenticated" ON master_articles FOR ALL TO authenticated USING (true) WITH CHECK (true);

-- Also add policies for 'anon' role if the app uses it for logged in users (common in some Supabase setups using custom auth)
-- But the task specifically mentioned 'authenticated access'.
-- However, memory says: "Since the application uses a custom authentication system relying on the Supabase 'anon' role, all database tables ... require Row Level Security (RLS) policies that explicitly grant the necessary permissions to the 'anon' role."
-- So I should probably keep 'anon' too, or both.

CREATE POLICY "Enable all for anon" ON master_departments FOR ALL TO anon USING (true) WITH CHECK (true);
CREATE POLICY "Enable all for anon" ON master_articles FOR ALL TO anon USING (true) WITH CHECK (true);
