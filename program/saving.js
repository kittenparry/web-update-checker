const rp = require('request-promise');
const cheerio = require('cheerio');
const path = require('path');
const fs = require('fs');

// testing url
const url = 'https://www.reddit.com/';

save = (body) => {
  dir = path.join(__dirname, 'saved_sites/test.txt');
  fs.writeFileSync(dir, body);
};
test = () => {
  rp(url)
  .then((html) => {
    // console.log(html);
    // console.log(cheerio.load(html));
    var $ = cheerio.load(html);
    $('body').each((index, element) => {
      console.log(element);
      save(element);
    });

    // var $ = cheerio.load(url);
    // $('div .thing').each((index, element) =>{
    // console.log(index);
    // console.log(element);
    // });
  })
  .catch((err) => {
    console.log(err);
  });
};

module.exports = test;
