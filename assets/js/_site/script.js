// JAVASCRIPT + FIRESTORE TUTORIAL //
// https://www.freecodecamp.org/news/the-firestore-tutorial-for-2020-learn-by-example/

// with Commonjs syntax (if using Node)
//const firebase = require("firebase/app");
//require("firebase/firestore");

// with ES Modules (if using client-side JS, like React)
import firebase from 'firebase/app';
import 'firebase/firestore';

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyCxkF6Ls9rKf8InKjLA5LkCVBYm1k2CsPU",
  authDomain: "datafaux-ab0de.firebaseapp.com",
  // 🚨 Do I need a databaseURL here!?!? 🚨
  projectId: "datafaux-ab0de",
  storageBucket: "datafaux-ab0de.appspot.com",
  messagingSenderId: "14595203943",
  appId: "1:14595203943:web:17b6a8d2121b2278ae45c2"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// This gives us access to all the methods of firebase firestore
const db = firebase.firestore();

// Use .collection() to reference a collections
// We can get a reference to books collection, we can pass .collection('books')
const booksRef = firebase.firestore().collection('books');

// Combines the variables defined above
const booksRef = firebase
  .firestore()
  .collection("books");

// .get() will return all the data within our collection at single given time
booksRef
  .get() // returns a promise...🤔
  .then((snapshot) => {
    const data = snapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    console.log("All data in 'books' collection", data);
    // [ { id: 'glMeZvPpTN1Ah31sKcnj', title: 'The Great Gatsby' } ]
  });

// .onSnapshot() will return the current data within the collection, whenever
// it's updated
firebase
  .firestore()
  .collection("books")
  .onSnapshot((snapshot) => {
    const data = snapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    console.log("All data in 'books' collection", data);
  });
