import { Component } from '@angular/core';
import { LogInForm } from 'src/app/types/auth';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form: LogInForm = {
    email: '',
    password: ''
  };

  constructor(private authService: AuthService) {}

  submit() {
    this.authService.login(this.form);
  }
  isLoading() {
    return this.authService.isLoading;
  }
}
