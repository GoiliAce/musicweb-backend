# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail_url = models.TextField(blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    date_create = models.TextField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Album'


class Artist(models.Model):
    id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    follow = models.IntegerField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    alias = models.TextField(primary_key=True)
    songs = models.ManyToManyField('Song', through='Artistsong')
    class Meta:
        managed = False
        db_table = 'Artist'


class Artistsong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'ArtistSong'


class Playlist(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    songs = models.ManyToManyField('Song', through='Playlistsong')
    class Meta:
        managed = False
        db_table = 'Playlist'


class Playlistbyuser(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistByUser'


class Playlistbyusersong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    playlist = models.ForeignKey(Playlistbyuser, models.DO_NOTHING)
    date_add = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistByUserSong'


class Playlistsong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING, blank=True, null=True)
    playlist = models.ForeignKey(Playlist, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistSong'


class Playlistuser(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    playlist_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistUser'


class Song(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    audio = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    artists = models.ManyToManyField(Artist, through='Artistsong')
    playlists = models.ManyToManyField(Playlist, through='Playlistsong')
    class Meta:
        managed = False
        db_table = 'Song'


class Topic(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Topic'


class User(models.Model):
    user_name = models.TextField(primary_key=True)
    passwd = models.TextField()
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Usersongs(models.Model):
    song = models.ForeignKey(Song, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    islike = models.BooleanField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    recenly_listen_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserSongs'
