const fs = require('fs');
const path = require('path');
const os = require('os');

const saved_sites = path.join(__dirname, 'saved_sites');
const site_names = path.join(__dirname, 'site_names.txt');

// check if saved_sites folder exists, create if not
check_sites_folder = () => {
  if(!fs.existsSync(saved_sites)){
    fs.mkdirSync(saved_sites);
  }
};
// check if site_names.txt exists, create if not
check_site_names = () => {
  if(fs.existsSync(site_names)){
    var temp = fs.readFileSync(site_names, 'utf8').split(os.EOL);
    var read = [];
    for(var el of temp){
      // don't accept comments and empty lines
      if(!el.startsWith('#') && el !== ''){
        read.push(el);
      }
    }
    return read;
  }else{
    // print instructions with # in before
    // this also sets file EOL to current OS
    // possible read errors above if the file is shared across OSes
    var instructions = `# Paste website names one per line${os.EOL}`;
    fs.writeFileSync(site_names, instructions);
    return check_site_names();
  }
};

module.exports = {
  name_folder: saved_sites,
  name_sites: site_names,
  check_site_names: check_site_names,
  check_sites_folder: check_sites_folder
};
