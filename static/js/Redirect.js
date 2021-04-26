function postData(input) {
        console.log("response");
    $.ajax({
        type: "POST",
        url: "C:/Users/91887/Documents/atharva/pythonprac/OpenCV/DinoGame.py",
        data: { param: input },
        success: callbackFunc

    });
}

function callbackFunc(response) {
    console.log(response);
}
    function myFunction() {
      postData('data to process');
      //window.location.href = "https://chromedino.com/";
      
      // var objShell = new ActiveXObject("shell.application");
      // objShell.ShellExecute("cmd.exe", "C:Users\\91887\\AppData\\Local\\Programs\\Python\\Python39\\python.exe", "C:\\WINDOWS\\system32", "open", 1);
//         var exec = require('child_process').exec, child;
// child = exec('python3 C:\\Users\\91887\\Document\\/atharva\\pythonprac\\OpenC\\(A9)DinoGame.py',
//     function (error, stdout, stderr) {
//         console.log('stdout: ' + stdout);
//         console.log('stderr: ' + stderr);
//         if (error !== null) {
//              console.log('exec error: ' + error);
//         }
//     });
// child();

      }
