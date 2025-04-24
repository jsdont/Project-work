import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PhotoService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getPhotos(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/photos/`);
  }

  getQuests(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/quests/`);
  }
}
