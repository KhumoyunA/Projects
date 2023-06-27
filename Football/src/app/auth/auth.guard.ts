import { CanActivate, CanActivateFn } from '@angular/router';
import { AuthService } from './auth.service';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})

export class authGuard  implements CanActivate {

  constructor(private authService: AuthService ) {
  }
  canActivate() {
    return this.authService.isAuthenticated;
  }
    
};
