import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { PlayersModule } from './players/players.module';
import { FavoritesComponent } from './favorites/favorites.component';
import { AuthModule } from './auth/auth/auth.module';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    FavoritesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    PlayersModule,
    AuthModule,
    HttpClientModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
