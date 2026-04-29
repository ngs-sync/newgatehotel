const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('index.html');
  console.log('Loading:', filePath);

  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
  page.on('pageerror', err => console.log('BROWSER ERROR:', err.message));

  await page.goto(filePath);
  await page.waitForTimeout(5000);

  const rootContent = await page.innerHTML('#root');
  if (rootContent.trim().length > 0) {
    console.log('React rendered successfully.');
  } else {
    console.log('React failed to render.');
  }

  await browser.close();
})();
