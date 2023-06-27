import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FavoritesService } from 'src/app/favorites/favorites.service';
import { AuthService } from 'src/app/auth/auth.service';
import { PlayersService } from '../players.service';
import { PlayerAPi, Response } from 'src/app/types/playerAPI';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.css']
})


export class PlayerComponent {
  isFavorite: boolean = false;
  @Input() player?: Response;
  @Input() index?: number;

  addToFav() {
    this.isFavorite = true;
    if (this.player) {
       this.favoritesService.add(this.player.player.name);
    }
   
  }

  remove() {
    this.isFavorite = false;
    if (this.player) {
      this.favoritesService.remove(this.player.player.name);
   }
  }

  constructor(private favoritesService: FavoritesService, private playersService: PlayersService, private authService: AuthService) {}


  isAuthenticated() {
   return this.authService.isAuthenticated;
  }


}
