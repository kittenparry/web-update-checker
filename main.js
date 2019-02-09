const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;

let main_window;

// TODO: comment in
// const win_w = 400;
// const win_h = 750;
const win_w = 750;
const win_h = 750;

//app ready
app.on('ready', () => {
  const screen = electron.screen.getPrimaryDisplay().size;
  const screen_w = screen.width;
  const screen_h = screen.height;
  //create window
  main_window = new BrowserWindow({
    width: win_w,
    height: win_h,
    // spawns window to the right of the screen
    // TODO: comment in
    // x: screen_w - win_w,
    // y: (screen_h - win_h) / 2,
  });
  //load html into the window
  //file://dirname/main_window.html
  main_window.loadURL(url.format({
    pathname: path.join(__dirname, 'program/window.html'),
    protocol: 'file',
    slashes: true,
  }));
  //quit on main window close
  main_window.on('closed', () => {
    app.quit();
    main_window = null;
  });
  //build menu from template
  const main_menu = Menu.buildFromTemplate(main_menu_template);
  //insert menu
  Menu.setApplicationMenu(main_menu);
  //start with dev tools opened
  main_window.webContents.openDevTools();
});
//menu template
const main_menu_template = [
  {
    label: 'File',
    submenu: [
      {
        label: 'Close',
        accelerator: process.platform == 'darwin' ? 'Command+Q' : 'Ctrl+Q',
        click(){
          app.quit();
        }
      }
    ]
  }
];
//if mac, add empty object to menu
if(process.platform == 'darwin'){
  main_menu_template.unshift({});
}
//dev tools when not in production
if(process.env.NODE_ENV !== 'production'){
  main_menu_template.push({
    label: 'Dev Tools',
    submenu: [
      {
        label: 'Toggle',
        accelerator: process.platform == 'darwin' ? 'Command+I' : 'Ctrl+I',
        click(item, focusedWindow){
          focusedWindow.toggleDevTools();
        }
      },
      {
        role: 'reload'
      }
    ]
  });
}
