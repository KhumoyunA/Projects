export interface PlayerAPi {
  get: string
  parameters: Parameters
  errors: any[]
  results: number
  paging: Paging
  response: Response[]
}

export interface Parameters {
  league: string
  season: string
}

export interface Paging {
  current: number
  total: number
}

export interface Response {
  player: Player
  statistics: Statistic[]
}

export interface Player {
  id: number
  name: string
  firstname: string
  lastname: string
  age: number
  birth: Birth
  nationality: string
  height: string
  weight: string
  injured: boolean
  photo: string
}

export interface Birth {
  date: string
  place: string
  country: string
}

export interface Statistic {
  team: Team
  league: League
  games: Games
  substitutes: Substitutes
  shots: Shots
  goals: Goals
  passes: Passes
  tackles: Tackles
  duels: Duels
  dribbles: Dribbles
  fouls: Fouls
  cards: Cards
  penalty: Penalty
}

export interface Team {
  id: number
  name: string
  logo: string
}

export interface League {
  id: number
  name: string
  country: string
  logo: string
  flag: string
  season: number
}

export interface Games {
  appearences: number
  lineups: number
  minutes: number
  number: any
  position: string
  rating: string
  captain: boolean
}

export interface Substitutes {
  in: number
  out: number
  bench: number
}

export interface Shots {
  total: number
  on: number
}

export interface Goals {
  total: number
  conceded: any
  assists: number
  saves: any
}

export interface Passes {
  total: number
  key: number
  accuracy: number
}

export interface Tackles {
  total: number
  blocks: number
  interceptions: number
}

export interface Duels {
  total: number
  won: number
}

export interface Dribbles {
  attempts: number
  success: number
  past: any
}

export interface Fouls {
  drawn: number
  committed: number
}

export interface Cards {
  yellow: number
  yellowred: number
  red: number
}

export interface Penalty {
  won: number
  commited: any
  scored: number
  missed: number
  saved: any
}

