import re

content = open('index.html').read()
script_start_marker = '<script type="text/babel">'
script_end_marker = '</script>'

new_script = r"""
        const SUPABASE_URL = 'https://wzammfnzptusiicwdaut.supabase.co';
        const SUPABASE_ANON_KEY = 'sb_publishable_Jk23sVPoYwengKLIjL78ww_Az4d7Tl-';
        const GEMINI_API_KEY = 'AIzaSyA92TBUTDqARe9mcVI7uTChuRGYe6vK9RY';

        const isConfigured = SUPABASE_URL.startsWith('http');
        const supabase = isConfigured ? window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY) : null;

        const { useState, useEffect } = React;

        const Icons = {
            Home: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>,
            Book: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>,
            Bed: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>,
            Logout: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>,
            Plus: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 4v16m8-8H4"></path></svg>,
            Close: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path></svg>,
            Sparkles: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>,
            Settings: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>,
            Trash: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>,
            Edit: () => <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
        };

        const Toast = ({ message, type, onClose }) => {
            useEffect(() => {
                const timer = setTimeout(onClose, 3000);
                return () => clearTimeout(timer);
            }, [message]);
            if (!message) return null;
            const bg = type === 'error' ? 'bg-red-500' : 'bg-green-500';
            return (
                <div className={`fixed top-5 right-5 ${bg} text-white px-6 py-3 rounded-lg shadow-lg flex items-center z-50`}>
                    <span>{message}</span>
                </div>
            );
        };

        const LoginScreen = ({ onLoginSuccess, showToast }) => {
            const [loading, setLoading] = useState(false);
            const [formData, setFormData] = useState({ tenant_id: '', email: '', password: '' });

            const handleLogin = async (e) => {
                e.preventDefault();
                setLoading(true);
                try {
                    const { data, error } = await supabase
                        .from('profiles')
                        .select('*, tenants(name)')
                        .eq('tenant_id', formData.tenant_id.toUpperCase())
                        .eq('email', formData.email)
                        .eq('password', formData.password)
                        .maybeSingle();

                    if (error) throw new Error("Database error.");
                    if (!data) throw new Error("Login gagal.");

                    showToast(`Selamat datang, ${data.full_name}!`, "success");
                    localStorage.setItem('hotel_session', JSON.stringify(data));
                    onLoginSuccess(data);
                } catch (error) {
                    showToast(error.message, "error");
                } finally {
                    setLoading(false);
                }
            };

            return (
                <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
                    <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md">
                        <div className="text-center mb-8">
                            <h1 className="text-3xl font-bold text-blue-600">New Gates PMS</h1>
                        </div>
                        <form onSubmit={handleLogin} className="space-y-5">
                            <input type="text" required className="w-full border p-3 rounded-lg uppercase" placeholder="Kode Hotel"
                                value={formData.tenant_id} onChange={(e) => setFormData({...formData, tenant_id: e.target.value.trim()})} />
                            <input type="email" required className="w-full border p-3 rounded-lg" placeholder="Email"
                                value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value.trim()})} />
                            <input type="password" required className="w-full border p-3 rounded-lg" placeholder="Password"
                                value={formData.password} onChange={(e) => setFormData({...formData, password: e.target.value})} />
                            <button type="submit" disabled={loading} className="w-full bg-blue-600 text-white font-bold py-3 rounded-lg">
                                {loading ? 'Checking...' : 'Login'}
                            </button>
                        </form>
                    </div>
                </div>
            );
        };

        const AIAssistantView = ({ showToast }) => {
            const [prompt, setPrompt] = useState('');
            const [response, setResponse] = useState('');
            const [loading, setLoading] = useState(false);

            const handleAskAI = async (e) => {
                e.preventDefault();
                setLoading(true);
                try {
                    const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
                    });
                    const data = await res.json();
                    setResponse(data.candidates[0].content.parts[0].text);
                    setPrompt('');
                } catch (error) {
                    showToast(error.message, "error");
                } finally { setLoading(false); }
            };

            return (
                <div className="space-y-6">
                    <h2 className="text-2xl font-bold">AI Assistant</h2>
                    <div className="bg-white p-6 rounded-xl shadow-sm h-[60vh] flex flex-col">
                        <div className="flex-1 overflow-y-auto mb-4 bg-gray-50 p-4 rounded-lg">
                            {loading ? "Thinking..." : <div dangerouslySetInnerHTML={{ __html: response.replace(/\n/g, '<br/>') }}></div>}
                        </div>
                        <form onSubmit={handleAskAI} className="flex gap-2">
                            <input type="text" className="flex-1 border p-2 rounded" value={prompt} onChange={e=>setPrompt(e.target.value)} />
                            <button type="submit" className="bg-purple-600 text-white px-4 py-2 rounded">Ask</button>
                        </form>
                    </div>
                </div>
            );
        };

        const Dashboard = ({ tenantId }) => {
            const [stats, setStats] = useState({ rooms: 0, res: 0 });
            useEffect(() => {
                supabase.from('rooms').select('id', { count: 'exact' }).eq('tenant_id', tenantId).then(r => setStats(s => ({...s, rooms: r.count || 0})));
            }, [tenantId]);
            return (
                <div className="p-6 bg-white rounded-xl shadow-sm">
                    <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
                    <p>Total Kamar: {stats.rooms}</p>
                </div>
            );
        };

        const RoomsView = ({ tenantId }) => {
            const [rooms, setRooms] = useState([]);
            useEffect(() => {
                supabase.from('rooms').select('*').eq('tenant_id', tenantId).order('room_number').then(r => setRooms(r.data || []));
            }, [tenantId]);
            return (
                <div className="space-y-4">
                    <h2 className="text-2xl font-bold">Housekeeping</h2>
                    <div className="grid grid-cols-4 gap-4">
                        {rooms.map(r => <div key={r.id} className="p-4 bg-white rounded-lg shadow-sm text-center font-bold">{r.room_number}</div>)}
                    </div>
                </div>
            );
        };

        const ReservationsView = ({ tenantId }) => {
            return <div className="p-6 bg-white rounded-xl shadow-sm"><h2 className="text-2xl font-bold">Front Office</h2><p>Data Reservasi...</p></div>;
        };

        const RoomCategorySetting = ({ tenantId, showToast }) => {
            const [categories, setCategories] = useState([]);
            const [isModalOpen, setIsModalOpen] = useState(false);
            const [form, setForm] = useState({ name: '', bed_type: '' });

            const fetch = () => supabase.from('room_categories').select('*').eq('tenant_id', tenantId).order('name').then(r => setCategories(r.data || []));
            useEffect(() => { fetch(); }, []);

            const handleSubmit = async (e) => {
                e.preventDefault();
                await supabase.from('room_categories').insert([{...form, tenant_id: tenantId}]);
                setIsModalOpen(false); fetch();
            };

            return (
                <div className="space-y-4">
                    <div className="flex justify-between">
                        <h3 className="font-bold">Room Category</h3>
                        <button onClick={() => setIsModalOpen(true)} className="bg-blue-600 text-white px-3 py-1 rounded">Add</button>
                    </div>
                    <table className="w-full text-left">
                        <thead><tr className="border-b"><th>Name</th><th>Bed</th><th>Action</th></tr></thead>
                        <tbody>
                            {categories.map(c => <tr key={c.id} className="border-b"><td>{c.name}</td><td>{c.bed_type}</td><td><button onClick={() => supabase.from('room_categories').delete().eq('id', c.id).then(fetch)} className="text-red-500">Delete</button></td></tr>)}
                        </tbody>
                    </table>
                    {isModalOpen && (
                        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4">
                            <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg w-full max-w-sm space-y-4">
                                <input required placeholder="Name" className="w-full border p-2 rounded" value={form.name} onChange={e=>setForm({...form, name: e.target.value})} />
                                <input required placeholder="Bed" className="w-full border p-2 rounded" value={form.bed_type} onChange={e=>setForm({...form, bed_type: e.target.value})} />
                                <div className="flex justify-end gap-2"><button type="button" onClick={()=>setIsModalOpen(false)}>Cancel</button><button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Save</button></div>
                            </form>
                        </div>
                    )}
                </div>
            );
        };

        const RoomNumberSetting = ({ tenantId, showToast }) => {
            const [rooms, setRooms] = useState([]);
            const [categories, setCategories] = useState([]);
            const [isModalOpen, setIsModalOpen] = useState(false);
            const [selectedCat, setSelectedCat] = useState('');
            const [bulkRows, setBulkRows] = useState([{num: ''}]);

            const fetch = async () => {
                const [r1, r2] = await Promise.all([supabase.from('rooms').select('*, room_categories(name)').eq('tenant_id', tenantId).order('room_number'), supabase.from('room_categories').select('*').eq('tenant_id', tenantId)]);
                setRooms(r1.data || []); setCategories(r2.data || []);
            };
            useEffect(() => { fetch(); }, []);

            const handleSubmit = async (e) => {
                e.preventDefault();
                const payload = bulkRows.filter(r=>r.num).map(r=>({room_number: r.num, tenant_id: tenantId, category_id: selectedCat, status: 'available'}));
                if (payload.length) await supabase.from('rooms').insert(payload);
                setIsModalOpen(false); fetch();
            };

            return (
                <div className="space-y-4">
                    <div className="flex justify-between">
                        <h3 className="font-bold">Room Numbers</h3>
                        <button onClick={() => setIsModalOpen(true)} className="bg-blue-600 text-white px-3 py-1 rounded">Bulk Add</button>
                    </div>
                    <table className="w-full text-left">
                        <thead><tr className="border-b"><th>Number</th><th>Type</th><th>Action</th></tr></thead>
                        <tbody>
                            {rooms.map(r => <tr key={r.id} className="border-b"><td>{r.room_number}</td><td>{r.room_categories?.name}</td><td><button onClick={() => supabase.from('rooms').delete().eq('id', r.id).then(fetch)} className="text-red-500">Delete</button></td></tr>)}
                        </tbody>
                    </table>
                    {isModalOpen && (
                        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4">
                            <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg w-full max-w-lg space-y-4">
                                <select required value={selectedCat} onChange={e=>setSelectedCat(e.target.value)} className="w-full border p-2 rounded">
                                    <option value="">Select Type</option>
                                    {categories.map(c=><option key={c.id} value={c.id}>{c.name}</option>)}
                                </select>
                                {bulkRows.map((r, i) => (
                                    <input key={i} placeholder="Room Number" className="w-full border p-2 rounded" value={r.num} onChange={e=>{const n=[...bulkRows]; n[i].num=e.target.value; setBulkRows(n);}} />
                                ))}
                                <button type="button" onClick={()=>setBulkRows([...bulkRows, {num:''}])} className="text-blue-600">+ Add Row</button>
                                <div className="flex justify-end gap-2"><button type="button" onClick={()=>setIsModalOpen(false)}>Cancel</button><button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Save</button></div>
                            </form>
                        </div>
                    )}
                </div>
            );
        };

        const HotelConfigView = ({ session, showToast }) => {
            const [activeTab, setActiveTab] = useState('cat');
            return (
                <div className="space-y-6">
                    <h2 className="text-2xl font-bold">Configuration</h2>
                    <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
                        <div className="flex border-b">
                            <button onClick={()=>setActiveTab('cat')} className={`px-4 py-2 ${activeTab==='cat'?'border-b-2 border-blue-600':''}`}>Category</button>
                            <button onClick={()=>setActiveTab('num')} className={`px-4 py-2 ${activeTab==='num'?'border-b-2 border-blue-600':''}`}>Number</button>
                        </div>
                        <div className="p-6">
                            {activeTab==='cat' && <RoomCategorySetting tenantId={session.tenant_id} showToast={showToast} />}
                            {activeTab==='num' && <RoomNumberSetting tenantId={session.tenant_id} showToast={showToast} />}
                        </div>
                    </div>
                </div>
            );
        };

        const App = () => {
            const [session, setSession] = useState(null);
            const [view, setView] = useState('dashboard');
            const [toast, setToast] = useState({ m: '', t: '' });
            const showToast = (m, t='success') => setToast({ m, t });

            useEffect(() => {
                const s = localStorage.getItem('hotel_session');
                if (s) setSession(JSON.parse(s));
            }, []);

            if (!session) return <LoginScreen onLoginSuccess={setSession} showToast={showToast} />;

            const nav = [{id:'dashboard', l:'Dashboard'}, {id:'fo', l:'Front Office'}, {id:'hk', l:'Housekeeping'}, {id:'ai', l:'AI Assistant'}];
            if (session.role === 'hotel_admin') nav.push({id:'cfg', l:'Config'});

            return (
                <div className="flex h-screen bg-gray-100">
                    <div className="w-64 bg-white border-r flex flex-col">
                        <div className="p-6 font-bold text-blue-700 border-b">{session.tenants?.name || 'Hotel PMS'}</div>
                        <nav className="flex-1 p-4 space-y-2">
                            {nav.map(n => <button key={n.id} onClick={()=>setView(n.id)} className={`w-full text-left px-4 py-2 rounded-lg ${view===n.id?'bg-blue-50 text-blue-700 font-bold':''}`}>{n.l}</button>)}
                        </nav>
                        <div className="p-4 border-t"><button onClick={()=>{localStorage.removeItem('hotel_session'); setSession(null);}} className="text-red-600">Logout</button></div>
                    </div>
                    <div className="flex-1 overflow-y-auto p-8">
                        {view==='dashboard' && <Dashboard tenantId={session.tenant_id} />}
                        {view==='fo' && <ReservationsView tenantId={session.tenant_id} />}
                        {view==='hk' && <RoomsView tenantId={session.tenant_id} />}
                        {view==='ai' && <AIAssistantView showToast={showToast} />}
                        {view==='cfg' && <HotelConfigView session={session} showToast={showToast} />}
                    </div>
                    {toast.m && <Toast message={toast.m} type={toast.t} onClose={()=>setToast({m:'',t:''})} />}
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
"""

start_idx = content.find(script_start_marker) + len(script_start_marker)
end_idx = content.find(script_end_marker, start_idx)
final_content = content[:start_idx] + new_script + content[end_idx:]

with open('index.html', 'w') as f:
    f.write(final_content)
