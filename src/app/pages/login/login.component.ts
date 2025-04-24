import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username = '';
  password = '';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    const credentials = {
      username: this.username,
      password: this.password
    };

    this.authService.login(credentials).subscribe({
      next: (res: any) => {
        this.authService.saveToken(res.access);
        console.log('Успешный вход');
        this.router.navigate(['/upload']);
      },
      error: (err: any) => {
        console.error('Ошибка входа', err);
        alert('Неверные данные');
      }
    });
  }
}
