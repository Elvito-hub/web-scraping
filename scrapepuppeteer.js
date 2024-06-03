import puppeteer from "puppeteer-core";
import fs from 'fs';

async function run(){
    let browser;
    try {
        const auth = `${proxy_username}:${proxy_password}`;
        browser = await puppeteer.connect({
            browserWSEndpoint:`wss://${auth}@brd.superproxy.io:9222`
        })

        const page = await browser.newPage();

        page.setDefaultNavigationTimeout(2*60*1000);
        page.setCacheEnabled(false);
        
        await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36');
        await page.goto("https://turaheza.com/category/amazu-akodeshwa/");
        const selector = ".post-list";

        await page.waitForSelector(selector);
        const el = await page.$(selector);
        const html = await el.evaluate(e=>e.innerHTML);
        const housesInfo = await page.evaluate((html) => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const housesElms = doc.querySelectorAll('.post-title');

            const houses = [];
        
            housesElms.forEach((jobElement) => {
              const titleElement = jobElement.querySelector('a');
        
              const house = {
                title: titleElement ? titleElement.innerText.trim() : '',
            };
        
            houses.push(house);
            });
        
            return houses;
          }, html);
          

    } catch (error) {
        console.log('scrapping failed',error);
    }
    finally{
        await browser?.close();
    }
};

run();

