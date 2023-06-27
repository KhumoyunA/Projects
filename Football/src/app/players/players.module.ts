import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PlayersService } from './players.service';
import { PlayerComponent } from './player/player.component';
import { PlayersComponent } from './players.component';
import { FormsModule } from '@angular/forms';




@NgModule({
  declarations: [ PlayerComponent, PlayersComponent],
  imports: [CommonModule, FormsModule],
  providers: [PlayersService],
  exports: [PlayersComponent]
})


export class PlayersModule { }
