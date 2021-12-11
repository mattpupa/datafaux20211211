
// Guide for setting up authentication
// https://firebase.google.com/docs/auth/web/firebaseui?authuser=0

var auth = firebase.auth();
//auth.useEmulator("http://localhost:9099");

// Initialize the FirebaseUI Widget using Firebase.
var ui = new firebaseui.auth.AuthUI(auth);

ui.start('#firebaseui-auth-container', {
  signInOptions: [
    firebase.auth.EmailAuthProvider.PROVIDER_ID
    //,signInMethod: firebase.auth.EmailAuthProvider.EMAIL_LINK_SIGN_IN_METHOD
  ],
  // Other config options...
});

var uiConfig = {
  callbacks: {
    signInSuccessWithAuthResult: function(authResult, redirectUrl) {
      var user = authResult.user;
      var credential = authResult.credential;
      var isNewUser = authResult.additionalUserInfo.isNewUser;
      var providerId = authResult.additionalUserInfo.providerId;
      var operationType = authResult.operationType;
      // User successfully signed in.
      // Return type determines whether we continue the redirect automatically
      // or whether we leave that to developer to handle.
      return true;
    },
    signInFailure: function(error) {
            // Some unrecoverable error occurred during sign-in.
            // Return a promise when error handling is completed and FirebaseUI
            // will reset, clearing any UI. This commonly occurs for error code
            // 'firebaseui/anonymous-upgrade-merge-conflict' when merge conflict
            // occurs. Check below for more details on this.
            return handleUIError(error);
    },
    uiShown: function() {
      // The widget is rendered.
      // Hide the loader.
      document.getElementById('loader').style.display = 'none';
    }
  },
  // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
  signInFlow: 'popup',
  signInSuccessUrl: 'https://datafaux.com/ui.html',
  signInOptions: [
    // Leave the lines as is for the providers you want to offer your users.
    firebase.auth.EmailAuthProvider.PROVIDER_ID
  ],
  // Terms of service url.
  tosUrl: 'https://datafaux.com/',
  // Privacy policy url.
  privacyPolicyUrl: 'https://datafaux.com/'
};

// The start method will wait until the DOM is loaded.
ui.start('#firebaseui-auth-container', uiConfig);

// Set persistance!
// https://firebase.google.com/docs/auth/web/auth-state-persistence?authuser=0
auth.setPersistence(firebase.auth.Auth.Persistence.SESSION)
  .then(() => {
    // Existing and future Auth states are now persisted in the current
    // session only. Closing the window would clear any existing state even
    // if a user forgets to sign out.
    // ...
    // New sign-in will be persisted with session persistence.
    return firebase.auth().signInWithEmailAndPassword(email, password);
  })
  .catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
  });


// do certain thing based on whether user is signed in or not!
// https://firebase.google.com/docs/auth/web/manage-users?authuser=0#get_the_currently_signed-in_user
auth.onAuthStateChanged(function(user) {
  if (user) {
    console.log("user logged in: ", user)
    currentEmail = user.email;
    console.log('user name is: ', user.displayName)
  } else {
    console.log("user logged out currently")
  }
});



// Create a function to get the books in the books firestore collection
// https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/ --> const
// https://developer.mozilla.org/en-US/docs/Web/API/Document --> document
// https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById --> Element by ID
// https://www.w3schools.com/jsref/met_document_getelementbyid.asp

// https://www.w3schools.com/jsref/prop_checkbox_checked.asp --> checkbox checked()
// Functions to tell whether checkboxes are checked or not!
// Need to tie this to then the submit button is clicked to get final results
// x can probably be changed to any name
// ❗️❗️❗️ I think I need to add these functions to the html tags❗️❗️❗️

// USER INFO
function checkboxCompanychecked() {
  checkboxCompany = document.getElementById("checkboxCompany").checked;
}
function checkboxNamechecked() {
  checkboxName = document.getElementById("checkboxName").checked;
}
function checkboxUserIDchecked() {
  checkboxUserID = document.getElementById("checkboxUserID").checked;
  // document.getElementById("cbID").innerHTML = checkboxID; --> Test code for checkbox.checked()
}
function checkboxUsernamechecked() {
  checkboxUsername = document.getElementById("checkboxUsername").checked;
}
function checkboxJobchecked() {
  checkboxJob = document.getElementById("checkboxJob").checked;
}
// CONTACT INFO
function checkboxAddresschecked() {
  checkboxAddress = document.getElementById("checkboxAddress").checked;
}
function checkboxEmailchecked() {
  checkboxEmail = document.getElementById("checkboxEmail").checked;
}
function checkboxPhonechecked() {
  checkboxPhone = document.getElementById("checkboxPhone").checked;
}
function checkboxURLchecked() {
  checkboxURL = document.getElementById("checkboxURL").checked;
}
// CREDIT CARD INFO
function checkboxCreditCardFullchecked() {
  checkboxCreditCardFull = document.getElementById("checkboxCreditCardFull").checked;
}
function checkboxCreditCardProviderchecked() {
  checkboxCreditCardProvider = document.getElementById("checkboxCreditCardProvider").checked;
}
function checkboxCreditCardNumberchecked() {
  checkboxCreditCardNumber = document.getElementById("checkboxCreditCardNumber").checked;
}
function checkboxCreditCardExpirechecked() {
  checkboxCreditCardExpire = document.getElementById("checkboxCreditCardExpire").checked;
}
function checkboxCreditCardSecurityCodechecked() {
  checkboxCreditCardSecurityCode = document.getElementById("checkboxCreditCardSecurityCode").checked;
}
// BANK INFO
function checkboxBankCountrychecked() {
  checkboxBankCountry = document.getElementById("checkboxBankCountry").checked;
}
function checkboxBasicBankAccountchecked() {
  checkboxBasicBankAccount = document.getElementById("checkboxBasicBankAccount").checked;
}
function checkboxIntlBankAccountchecked() {
  checkboxIntlBankAccount = document.getElementById("checkboxIntlBankAccount").checked;
}
// CURRENCY INFO
function checkboxCurrencyNamechecked() {
  checkboxCurrencyName = document.getElementById("checkboxCurrencyName").checked;
}
function checkboxCurrencyCodechecked() {
  checkboxCurrencyCode = document.getElementById("checkboxCurrencyCode").checked;
}
function checkboxCryptoCurrencyNamechecked() {
  checkboxCryptoCurrencyName = document.getElementById("checkboxCryptoCurrencyName").checked;
}
function checkboxCryptoCurrencyCodechecked() {
  checkboxCryptoCurrencyCode = document.getElementById("checkboxCryptoCurrencyCode").checked;
}
// DATE INFO
function checkboxAmPmchecked() {
  checkboxAmPm = document.getElementById("checkboxAmPm").checked;
}
function checkboxDatechecked() {
  checkboxDate = document.getElementById("checkboxDate").checked;
}
function checkboxDayofMonthchecked() {
  checkboxDayofMonth = document.getElementById("checkboxDayofMonth").checked;
}
function checkboxDayofWeekchecked() {
  checkboxDayofWeek = document.getElementById("checkboxDayofWeek").checked;
}
function checkboxMonthchecked() {
  checkboxMonth = document.getElementById("checkboxMonth").checked;
}
function checkboxMonthNamechecked() {
  checkboxMonthName = document.getElementById("checkboxMonthName").checked;
}
function checkboxYearchecked() {
  checkboxYear = document.getElementById("checkboxYear").checked;
}
// COLOR INFO
function checkboxColorNamechecked() {
  checkboxColorName = document.getElementById("checkboxColorName").checked;
}
function checkboxWebSafeColorNamechecked() {
  checkboxWebSafeColorName = document.getElementById("checkboxWebSafeColorName").checked;
}
function checkboxHexColorchecked() {
  checkboxHexColor = document.getElementById("checkboxHexColor").checked;
}
function checkboxRGBColorchecked() {
  checkboxRGBColor = document.getElementById("checkboxRGBColor").checked;
}
function checkboxRGBCSSColorchecked() {
  checkboxRGBCSSColor = document.getElementById("checkboxRGBCSSColor").checked;
}
// MISCELLANEOUS INFO
function checkboxBarcodeEAN8checked() {
  checkboxBarcodeEAN8 = document.getElementById("checkboxBarcodeEAN8").checked;
}
function checkboxBarcodeEAN13checked() {
  checkboxBarcodeEAN13 = document.getElementById("checkboxBarcodeEAN13").checked;
}
function checkboxImageURLchecked() {
  checkboxImageURL = document.getElementById("checkboxImageURL").checked;
}
function checkboxLatitudechecked() {
  checkboxLatitude = document.getElementById("checkboxLatitude").checked;
}
function checkboxLongitudechecked() {
  checkboxLongitude = document.getElementById("checkboxLongitude").checked;
}
function checkboxLicensePlatechecked() {
  checkboxLicensePlate = document.getElementById("checkboxLicensePlate").checked;
}

// !!!!! START AGAIN HERE !!!!!!!
// form functions
// https://developer.mozilla.org/en-US/docs/Web/API/Event --> Event
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events --> Event Handler
// https://www.w3schools.com/jsref/event_preventdefault.asp --> event.preventDefault

// This function seems to add a book to the collection if the input is in the correct format.
// If not, then the preventDefault() function runs instead
function handleCreate(event) { // handleCreate() seems to be named function, not existing
  event.preventDefault(); // This seems to prevent the page from refreshing. Test later!
  let datasetRequest = { //
    id: String(checkboxUserID)
    ,username: String(checkboxUsername)
    ,name: String(checkboxName)
    ,email: String(checkboxEmail)
    ,address: String(checkboxAddress)
    ,company: String(checkboxCompany)
    ,job: String(checkboxJob)
    ,phone: String(checkboxPhone)
    ,url: String(checkboxURL)
    ,creditcardfull: String(checkboxCreditCardFull)
    ,creditcardprovider: String(checkboxCreditCardProvider)
    ,creditcardnumber: String(checkboxCreditCardNumber)
    ,creditcardexpire: String(checkboxCreditCardExpire)
    ,creditcardsecuritycode: String(checkboxCreditCardSecurityCode)
    ,bankcountry: String(checkboxBankCountry)
    ,bban: String(checkboxBasicBankAccount)
    ,iban: String(checkboxIntlBankAccount)
    ,currencyname: String(checkboxCurrencyName)
    ,currencycode: String(checkboxCurrencyCode)
    ,cryptocurrencyname: String(checkboxCryptoCurrencyName)
    ,cryptocurrencycode: String(checkboxCryptoCurrencyCode)
    ,ampm: String(checkboxAmPm)
    ,date: String(checkboxDate)
    ,dayofmonth: String(checkboxDayofMonth)
    ,dayofweek: String(checkboxDayofWeek)
    ,month: String(checkboxMonth)
    ,monthname: String(checkboxMonthName)
    ,year: String(checkboxYear)
    ,colorname: String(checkboxColorName)
    ,websafecolorname: String(checkboxWebSafeColorName)
    ,hexcolor: String(checkboxHexColor)
    ,rgbcolor: String(checkboxRGBColor)
    ,rgbcsscolor: String(checkboxRGBCSSColor)
    ,ean8: String(checkboxBarcodeEAN8)
    ,ean13: String(checkboxBarcodeEAN13)
    ,imageurl: String(checkboxImageURL)
    ,latitude: String(checkboxLatitude)
    ,longitude: String(checkboxLongitude)
    ,licenseplate: String(checkboxLicensePlate)
    ,currentUserEmail: String(currentEmail)
  };
  return firebase
    .firestore()
    .collection("datasetRequests")
    .add(datasetRequest)
    .then(function (ref) {
      console.log("Added doc with ID: ", ref.id);
      console.log('currentUser email is: ', currentEmail);
      window.location.href="http://datafaux.com/confirm.html";
    // Added doc with ID:  ZzhIgLqELaoE3eSsOazu
    });
  $( 'input[type="checkbox"]' ).prop('checked', false);
}
// ❗️❗️❗️ Figure out how to set unchecked boxes to false instead of the HTML object

// ❗️❗️❗️ Figure out how to reset checkboxes after hitting submit!
// This resets html form, but also need to reset checked()
function resetForm() {
  document.getElementById("dataFieldsForm").reset();
}

function emailConfirm() {
  var text = document.getElementById("conf");
  if (text.style.display === "none") {
    text.style.display = "block";
  };
  let emailConfirm = { //
    currentUserEmail: String(currentEmail)
  };
  return firebase
    .firestore()
    .collection("emailConfirms")
    .add(emailConfirm)
    .then(function (ref) {
      console.log('Added email as: ', currentEmail);
    // Added doc with ID:  ZzhIgLqELaoE3eSsOazu
    });
};



/*
// Track data request fields in form
const checkboxUserID = document.getElementById("checkboxUserID").checked;
const checkboxUsername = document.getElementById("checkboxUsername").checked;
const checkboxName = document.getElementById("checkboxName").checked;
const checkboxEmail = document.getElementById("checkboxEmail").checked;
const checkboxAddress = document.getElementById("checkboxAddress").checked;
const checkboxCompany = document.getElementById("checkboxCompany").checked;
const checkboxDate = document.getElementById("checkboxDate").checked;

// Create new data request
const createRequest = document.querySelector('#dataFieldsForm');
createRequest.addEventListener('submit', function(event) {
  event.preventDefault();
  firebase.firestore().collection("datasetRequests").add({
    userID: String(createRequest['checkboxUserID'].value)
    ,userName: String(createRequest['checkboxUsername'].value)
    ,name: String(createRequest['checkboxName'].value)
    ,email: String(createRequest['checkboxEmail'].value)
    ,address: String(createRequest['checkboxAddress'].value)
    ,company: String(createRequest['checkboxCompany'].value)
    ,date: String(createRequest['checkboxDate'].value)
    ,currentUserEmail: String(user.email)
  }).then(function() {
    console.log('Data request sent to firebase');
    createRequest.reset();
  });
});
*/
