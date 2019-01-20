import firebase from 'firebase'
// Initialize Firebase
var config = {
	apiKey: "AIzaSyBfM8-rhGMIHFRC4oNmLrIof-t-uHTDenk",
	authDomain: "wittyhacks2019.firebaseapp.com",
	databaseURL: "https://wittyhacks2019.firebaseio.com",
	projectId: "wittyhacks2019",
	storageBucket: "wittyhacks2019.appspot.com",
	messagingSenderId: "572600587185"
};

const app = firebase.initializeApp(config);

export const db = firebase.firestore();
