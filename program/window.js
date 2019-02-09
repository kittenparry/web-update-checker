const sites = require('./sites');
const saving = require('./saving');


main = () => {
  sites.check_sites_folder();
  var site_names = check_site_names();
  console.log(site_names);
};

main();
saving();
