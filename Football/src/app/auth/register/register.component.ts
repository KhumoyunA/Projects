import { Component } from '@angular/core';
import { RegisterForm } from 'src/app/types/register';
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})


export class RegisterComponent {
  regForm: RegisterForm = {
    email: '',
    password: '',
    confirmPassword: ''
  };

  constructor(private authService: AuthService) {}



  register() {

    this.authService.register(this.regForm);
  }

  isRegLoading() {
    return this.authService.isRegLoading;
  }

}
