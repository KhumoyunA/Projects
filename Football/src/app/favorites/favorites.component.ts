import { Component } from '@angular/core';
import { FavoritesService } from './favorites.service';

@Component({
  selector: 'app-favorites',
  templateUrl: './favorites.component.html',
  styleUrls: ['./favorites.component.css']
})
export class FavoritesComponent {
  constructor(private favoritesService: FavoritesService) {}
  
  getFavorites(){
    return this.favoritesService.get();
  }

}
