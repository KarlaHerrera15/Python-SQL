import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  unita: any[] = []; // Array che ospiterà i dati ricevuti da Flask

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.caricaDati('all'); // Carica tutto all'avvio
  }

  caricaDati(endpoint: string) {
    // IMPORTANTE: Sostituisci questo URL con quello del tuo Codespace (Porta 5000)
    const baseUrl = 'https://jubilant-bassoon-4jqww9wvj9q72p6p-5000.app.github.dev';
    
    this.http.get<any[]>(`${baseUrl}/${endpoint}`).subscribe({
      next: (data) => {
        this.unita = data;
      },
      error: (err) => console.error(err)
    });
}
}