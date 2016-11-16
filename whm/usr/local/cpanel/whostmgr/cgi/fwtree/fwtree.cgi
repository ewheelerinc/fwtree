#!/usr/bin/perl

use warnings;
use strict;
use CGI;

my $q = CGI->new();

if (defined($q->param("ipset"))) {
	open(my $fh_write, '>', '/etc/ipset.d/cpanel-admins');
	print $fh_write $q->param("ipset") . "\n";
	close($fh_write);
	system(q/ipset flush cpanel-admins/);
	system('ipset-helper');
}

open(my $fh_read, '<', '/etc/ipset.d/cpanel-admins');
my $ipset = do { local $/; <$fh_read> };
chomp($ipset);
close($fh_read);

print qq(
<html>
<body>
	<h1>IPs with ADMIN access:</h1>
	<form action="?" method="POST">
		<textarea rows=40 cols=80 name=ipset>$ipset</textarea>
		<br>
		<input type=submit value="Update" />
	</form>
</body>
</html>
);
