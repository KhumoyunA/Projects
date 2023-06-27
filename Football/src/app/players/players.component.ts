import { Component } from '@angular/core';
import { Player } from '../types/player';
import { PlayersService } from './players.service';
import {  PlayerAPi } from '../types/playerAPI';



@Component({
  selector: 'app-players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.css']
})


export class PlayersComponent {

  favorites: Player[] = [];  
  players?: PlayerAPi;
  selectedLeague: number = 140;
  selectedSeason: number = 2022;

  leagues: any[] = [
    { label: 'English Premier League', id: 39 },
    { label: 'La Liga ', id: 140 },
    { label: 'Serie A', id: 135 },
    { label: 'Bundesliga', id: 78 },
    { label: 'Ligue 1', id: 61 },
    { label: 'UEFA Champions League', id: 2 },
    { label: 'UEFA Europa League', id: 3 },
  ];

  seasons: any[] = [
    { label: '2022/2023', value: 2022 },
    { label: '2021/2022', value: 2021 },
    { label: '2020/2021', value: 2020 },
    { label: '2019/2020', value: 2019 },
    { label: '2018/2019', value: 2018 },
    { label: '2017/2018', value: 2017 },
    { label: '2016/2017', value: 2016 },
  ];

// NOTE: may have to put the method inside oninit.

  onOptionChangeLeague() {
    // Handle the option change event
    console.log(this.selectedLeague);
    this.getPlayers();
  }

  onOptionChangeSeason() {
    // Handle the option change event
    console.log(this.selectedSeason);
    this.getPlayers();
  }

  getPlayers() {
    this.playersService.getPlayers(this.selectedSeason, this.selectedLeague)
    .subscribe({
      next: (response: any) => {
        this.players = (response);
        console.log(this.players);
      } 
    })
  }

  ngOnInit(): void {
    this.getPlayers();
  }

  constructor(private playersService: PlayersService) {  }
}
