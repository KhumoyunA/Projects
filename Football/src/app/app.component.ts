import { Component, OnInit } from '@angular/core';
import { initializeApp } from 'firebase/app';
import { firebaseConfig } from './firebase.config';
import { AuthService } from './auth/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

 ngOnInit(): void {
   initializeApp(firebaseConfig);
 }

 constructor(private authSerivce: AuthService) {}

 isAuthenticated() {
  return this.authSerivce.isAuthenticated;
 }

 logout() {
  this.authSerivce.logout();
 }
}
