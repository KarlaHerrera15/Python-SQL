import { ApplicationConfig } from '@angular/core'; // Importa il tipo per configurare l'app Angular standalone
import { provideRouter } from '@angular/router'; // Funzione per configurare il routing
import { provideHttpClient } from '@angular/common/http'; // Fornisce il servizio HttpClient a tutta l'app

import { routes } from './app.routes'; // Importa le rotte definite nell'app

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes), // Attiva il sistema di routing usando le rotte definite
    provideHttpClient() // Abilita HttpClient per fare richieste HTTP (API, backend, ecc.)
  ]
};