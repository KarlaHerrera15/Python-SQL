import { Component, OnInit } from '@angular/core'; // Importa il decoratore Component e l'interfaccia OnInit
import { HttpClient } from '@angular/common/http'; // Importa HttpClient per effettuare richieste HTTP
import { CommonModule } from '@angular/common'; // Importa il modulo comune (direttive base come ngIf, ngFor)

@Component({
  selector: 'app-root', // Nome del componente usato nel tag HTML
  standalone: true, // Indica che il componente è standalone (non serve modulo Angular)
  imports: [CommonModule], // Moduli utilizzabili nel template HTML
  templateUrl: './app.component.html', // File HTML associato al componente
  styleUrls: ['./app.component.css'] // File CSS associato al componente
})
export class AppComponent implements OnInit { // Classe principale del componente
  unita: any[] = []; // Array che ospiterà i dati ricevuti dal backend (Flask)

  constructor(private http: HttpClient) {} // Iniezione del servizio HttpClient

  ngOnInit() {
    this.caricaDati('all'); // Metodo eseguito all'avvio del componente
  }

  caricaDati(endpoint: string) {
    // IMPORTANTE: URL base del backend (server Flask su Codespaces porta 5000)
    const baseUrl = 'https://jubilant-bassoon-4jqww9wvj9q72p6p-5000.app.github.dev';
    
    // Effettua una richiesta GET all'endpoint specificato
    this.http.get<any[]>(`${baseUrl}/${endpoint}`).subscribe({
      next: (data) => { // Se la richiesta ha successo
        this.unita = data; // Salva i dati ricevuti nell'array
      },
      error: (err) => console.error(err) // Gestione errore (stampa in console)
    });
  }
}