 /*
$(document).ready(function(){var token = {{status}};
if(token) $("#btn-next-page-email").trigger( "click" );
});*/
//var csrfmiddlewaretoken = '{{ csrf_token }}';
  function theAjax(uri,data){
 return $.ajax({
    type:"POST",
    dataType:"json",
    url: uri,
    data : data
 });
};
window.fbAsyncInit = function () {
    FB.init({
        appId: '1234007736673311',
        cookie: false,  // enable cookies to allow the server to access
        // the session
        xfbml: true,  // parse social plugins on this page
        version: 'v2.8' // use version 2.0
    });
};
// Load the SDK asynchronously
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
function fb_login() {
    FB.login(function (response) {
        if (response.authResponse) {
            //console.log('Welcome!  Fetching your information.... ');
            //console.log(response); // dump complete info
            access_token = response.authResponse.accessToken; //get access token
            user_id = response.authResponse.userID;
            console.log(response)
            console.log(access_token);
            data = {}
            data['accessToken'] = response.authResponse.accessToken;
    data['uid'] = response.authResponse.userID;
    data['csrfmiddlewaretoken']= csrfmiddlewaretoken;
    /*theAjax('/fbConnect/',data).done(function(response){
      console.log(response);
      if (response['status'] == 1)
        window.location = '/dashboard'
      else{
        getData = 'name='+response['context']['name'];
        if ('email' in response['context']) getData += '&email='+response['context']['email'];
        getData += '&uid='+response['context']['uid'];
        window.location = '/register/?'+getData;
      } 
    });*/
        } else {
            //user hit cancel button
            console.log('User cancelled login or did not fully authorize.');
        }
    }, {
        scope: 'public_profile'
    });
}