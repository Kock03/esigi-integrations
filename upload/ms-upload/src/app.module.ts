import { Module } from '@nestjs/common';
import { APP_GUARD } from '@nestjs/core';
import { MulterModule } from '@nestjs/platform-express';
import { AppController } from './app.controller';
import { AuthGuard } from './guards/auth.guard';
import { HttpModule } from '@nestjs/axios';

@Module({
  imports: [HttpModule, MulterModule.register({
    dest: './files',
  })],
  controllers: [AppController],
  providers: [
    // {
    //   provide: APP_GUARD,
    //   useClass: AuthGuard,
    // },
  ]

})
export class AppModule { }
