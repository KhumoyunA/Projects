import { Injectable } from '@angular/core';
import { createUserWithEmailAndPassword, getAuth, reauthenticateWithCredential, signInWithEmailAndPassword, signOut } from 'firebase/auth';
import { LogInForm } from '../types/auth';
import { RegisterForm } from '../types/register';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isAuthenticated: boolean = false;
  isLoading: boolean = false;
  isRegLoading: boolean = false;
  isaMatch: boolean = true;


  constructor(private router: Router) {
  }

  login(form: LogInForm) {
    if (this.isLoading) return;
    this.isLoading = true;
    const auth = getAuth();
    signInWithEmailAndPassword(auth, form.email, form.password)
      .then((userCredential) => {
        // Signed in 
        const user = userCredential.user;
        this.isAuthenticated = true;
        this.router.navigate(['']);
        
      })
      .catch((error) => {
        const errorCode = error.code;
        this.isAuthenticated = false;
        const errorMessage = error.message;
        alert('Sorry, we are not able to find the user you are requesting');
      }).finally(() => (this.isLoading = false));
  }

  register(regForm: RegisterForm) {
    if (regForm.password != regForm.confirmPassword) {
      this.isaMatch = false;
      return;
    }

    if (this.isRegLoading) return;
    this.isRegLoading = true;


    const auth = getAuth();
    createUserWithEmailAndPassword(auth, regForm.email, regForm.password)
    .then((userCredential) => {
      // Signed in 
      // const user = userCredential.user;
      this.isAuthenticated = true;
      // ...
    })
    .catch((error) => {
      this.isAuthenticated = false;
      const errorCode = error.code;
      const errorMessage = error.message;
      // ..
    }).finally(() => (this.isRegLoading = false));
    }

    logout() {
      const auth = getAuth();
      signOut(auth).then(() => {
        this.router.navigate(['login']);
        this.isAuthenticated = false;
      }).catch((error) => {

      });

    }
}
