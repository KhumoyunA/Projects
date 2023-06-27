import { Injectable } from '@angular/core';
import { Player } from '../types/player';
import { HttpClient, HttpClientModule, HttpHeaders, HttpParams } from '@angular/common/http'; 
import { PlayerAPi } from '../types/playerAPI';
import { Observable } from 'rxjs';

@Injectable()

export class PlayersService {

  constructor(private http: HttpClient ) { }

  url = 'https://api-football-beta.p.rapidapi.com/players/topscorers';
  XRapidAPIHeader = 'X-RapidAPI-Host';
  XRapidAPIHeaderValue = 'api-football-beta.p.rapidapi.com';
  XRapidAPIKey = 'X-RapidAPI-Key';
  XRapidAPIKeyValue = 'eb1c7875a8msh24c3e03d84677a8p1a213ajsnf9b05c6dda03';
  // eb1c7875a8msh24c3e03d84677a8p1a213ajsnf9b05c6dda03
  getPlayers(season: number, league: number): Observable<PlayerAPi> {
    return this.http.get<PlayerAPi>(this.url, {
       headers: new HttpHeaders()
      .set(this.XRapidAPIHeader, this.XRapidAPIHeaderValue)
      .set(this.XRapidAPIKey, this.XRapidAPIKeyValue),
      params: new HttpParams()
      .set('season', season)
      .set('league', league)
    });
  }
}

