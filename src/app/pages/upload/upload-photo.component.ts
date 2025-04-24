import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { AuthService } from '../../services/auth.service';
import { PhotoService } from '../../services/photo.service';

@Component({
  selector: 'app-upload-photo',
  templateUrl: './upload-photo.component.html',
  styleUrls: ['./upload-photo.component.css']
})
export class UploadPhotoComponent implements OnInit {
  selectedFile: File | null = null;
  previewUrl: string | ArrayBuffer | null = null;
  quests: any[] = [];
  selectedQuest: string = '';
  rating: number = 0;
  uploadSuccess: boolean = false;

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private photoService: PhotoService
  ) {}

  ngOnInit(): void {
    this.photoService.getQuests().subscribe({
      next: (data) => {
        this.quests = data;
      },
      error: (err) => {
        console.error('Ошибка при загрузке квестов:', err);
      }
    });
  }

  logout() {
    this.authService.logout();
    window.location.href = '/login';
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];

    const reader = new FileReader();
    if (this.selectedFile) {
      reader.readAsDataURL(this.selectedFile);
      reader.onload = () => {
        this.previewUrl = reader.result;
      };
    }
  }

  setRating(stars: number) {
    this.rating = stars;
  }

  uploadPhoto() {
    if (!this.selectedFile) return;

    const formData = new FormData();
    formData.append('photo', this.selectedFile);
    formData.append('comment', 'загружено с Angular');
    formData.append('quest', this.selectedQuest);
    formData.append('rating', this.rating.toString());

    this.http.post(`${environment.apiUrl}/submissions/`, formData).subscribe({
      next: res => {
        console.log('Загружено успешно');
        this.uploadSuccess = true;

        // Сброс формы
        this.selectedFile = null;
        this.previewUrl = null;
        this.rating = 0;
        this.selectedQuest = '';

        // Авто-скрытие сообщения
        setTimeout(() => {
          this.uploadSuccess = false;
        }, 3000);
      },
      error: err => {
        console.error('Ошибка загрузки', err);
      }
    });
  }
}
