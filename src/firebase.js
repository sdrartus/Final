import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage} from "firebase/storage";


const firebaseConfig = {
    apiKey: "AIzaSyAagspIL51GG1vXFIM574ptehBoG9H5G0A",
    authDomain: "finals-cf7f6.firebaseapp.com",
    projectId: "finals-cf7f6",
    storageBucket: "finals-cf7f6.appspot.com",
    messagingSenderId: "461773547955",
    appId: "1:461773547955:web:278e8584b63656f09283c6"
  };

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const auth = getAuth()
export const storage = getStorage();
export const db = getFirestore(); // export const db = getFirestore() -> this is the original