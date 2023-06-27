import { Injectable } from '@angular/core';
import { Player } from '../types/player';
import { filter } from 'rxjs';
import { Response } from '../types/playerAPI';

@Injectable({
  providedIn: 'root'
})

export class FavoritesService {
  favorites: string[] = [];

  add(player: string) {
    this.favorites.push(player);
  }

  remove(player: string) {
    this.favorites = this.favorites.filter(p => p != player);
  }

  get() {
    return this.favorites;
  }

  constructor() { }
}
