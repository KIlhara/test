#!/usr/bin/perl

use DBI;

my $choise = $ARGV[0];
my $name = $ARGV[1];
my $update = $ARGV[2];
my $genre = $ARGV[3];
my $developer = $ARGV[4];
my $languages = $ARGV[5];

my $host = "127.0.0.1";

my $port = "3306";

my $user = "root";

my $pass = "misha";

my $db = "game_war";

#*****************************
#   connection in database   #
#*****************************
$dbh = DBI->connect("DBI:mysql:$db:$host:$port",$user,$pass);

#*****************************
#    show data from table    #
#*****************************
if($choise eq 'show'){ 
  $sth = $dbh->prepare("select * from games;");
  $sth->execute;

  while($ref = $sth->fetchrow_arrayref){
    print "$$ref[0]."
    . "$$ref[1] "
    . "$$ref[2] "
    . "$$ref[3] "
    . "$$ref[4] \n";
  }
  $rs = $sth->finish;
}

#****************************
#  update data in database  #
#****************************
elsif($choise eq 'update_name'){
  $sth = $dbh->prepare("update games set name_game='$update' where id_game='$name';");
  $sth->execute;
  $rs = $sth->finish;
}

elsif($choise eq 'update_genre'){
  $sth = $dbh->prepare("update games set Genre='$update' where id_game='$name';");
  $sth->execute;
  $rs = $sth->finish;
}

elsif($choise eq 'update_developer'){
  $sth = $dbh->prepare("update games set Developer='$update' where id_game='$name';");
  $sth->execute;
  $rs = $sth->finish;
}

elsif($choise eq 'update_languages'){
  $sth = $dbh->prepare("update games set Languages='$update' where id_game='$name';");
  $sth->execute;
  $rs = $sth->finish;
}

#****************************
#    ADD data in database   #
#****************************
elsif($choise eq 'insert'){
  my $id = $name;
  my $name_g = $update;
  $sth = $dbh->prepare("insert into games values('$id','$name_g','$genre','$developer','$languages');");
  $sth->execute;
  $rs = $sth->finish;
}

#******************************
# deleting data from database #
#******************************
elsif($choise eq 'delete'){
  my $id = $name;
  $sth = $dbh->prepare("delete from games where id_game='$id';");
  $sth->execute;
  $rs = $sth->finish;
}

#*****************************
# select on ID from database #
#*****************************
elsif($choise eq 'select'){
  $sth = $dbh->prepare("select * from games where id_game='$name';");
  $sth->execute;
  while($ref = $sth->fetchrow_arrayref){
    print "$$ref[0]."
    . "$$ref[1] "
    . "$$ref[2] "
    . "$$ref[3] "
    . "$$ref[4] \n\n";
  }
  $rs = $sth->finish;
}
