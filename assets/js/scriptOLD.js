// Firebase App (the core Firebase SDK) is always required and must be listed first
// with ES Modules (if using client-side JS, like React)

//import firebase from 'firebase/app';

// Add the Firebase products that you want to use
// import 'firebase/analytics';
// import 'firebase/auth';

//import 'firebase/firestore';

// Your web app's Firebase configuration.
// This seems to be the python equivalent of the service generated key.
/*
var firebaseConfig = {
  apiKey: "AIzaSyCxkF6Ls9rKf8InKjLA5LkCVBYm1k2CsPU",
  authDomain: "datafaux-ab0de.firebaseapp.com",
  databaseURL: "https://datafaux-ab0de.firebaseio.com", //databaseURL wasn't in original firebaseConfig. Added it in
  projectId: "datafaux-ab0de",
  storageBucket: "datafaux-ab0de.appspot.com",
  messagingSenderId: "14595203943",
  appId: "1:14595203943:web:17b6a8d2121b2278ae45c2"
  // Will need measurmentID here when Analytics is added!
};
// Initialize Firebase...this seems similar to opening a database connection
// refer to https://firebase.google.com/docs/reference/admin/python/firebase_admin
// for more info on what initialize_app does in python.
//firebase.initializeApp(firebaseConfig);

// This gives us access to all the methods of firebase firestore
// This needs to be executed ever time we want to interact with our firestore
// databse, which is why we save it as a constant db. It's easy to refer to later
const db = firebase.firestore()


// Code to test firestore locally...does this work? 🤔
// https://firebase.google.com/docs/emulator-suite/connect_firestore#web
if (location.hostname === "localhost") {
  db.useEmulator("localhost", 8080);
}
*/
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
function checkboxIDchecked() {
  checkboxID = document.getElementById("checkboxID").checked;
  // document.getElementById("cbID").innerHTML = checkboxID; --> Test code for checkbox.checked()
}
function checkboxUsernamechecked() {
  checkboxUsername = document.getElementById("checkboxUsername").checked;
}
function checkboxNamechecked() {
  checkboxName = document.getElementById("checkboxName").checked;
}
function checkboxEmailchecked() {
  checkboxEmail = document.getElementById("checkboxEmail").checked;
}
function checkboxAddresschecked() {
  checkboxAddress = document.getElementById("checkboxAddress").checked;
}
function checkboxCompanychecked() {
  checkboxCompany = document.getElementById("checkboxCompany").checked;
}
function checkboxDatechecked() {
  checkboxDate = document.getElementById("checkboxDate").checked;
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
    id: String(checkboxID),
    userName: String(checkboxUsername),
    name: String(checkboxName),
    email: String(checkboxEmail),
    address: String(checkboxAddress),
    company: String(checkboxCompany),
    date: String(checkboxDate),
  };
  return firebase
    .firestore()
    .collection("datasetRequests")
    .add(datasetRequest)
    .then((ref) => {
      console.log("Added doc with ID: ", ref.id);
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
