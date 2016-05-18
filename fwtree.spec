Name: fwtree
Summary: Tree-driven firewall
Version: 1.0.1
Release: 9.el7
BuildArch: noarch
Group: Application
License: Restricted
Prefix: /
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ipset
Requires: aggregate
Conflicts: firewalld
AutoReqProv: no

%description

%build
cp /usr/src/fwtree-git/fwtree-1.0.1-9.el7.noarch.tar %{_builddir}/fwtree-1.0.1-9.el7.noarch.tar

%install
mkdir -p $RPM_BUILD_ROOT/
mv fwtree-1.0.1-9.el7.noarch.tar $RPM_BUILD_ROOT/fwtree-1.0.1-9.el7.noarch.tar
cd $RPM_BUILD_ROOT/
tar -xf $RPM_BUILD_ROOT/fwtree-1.0.1-9.el7.noarch.tar
rm $RPM_BUILD_ROOT/fwtree-1.0.1-9.el7.noarch.tar

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ "$(ls -A /etc/iptables.d/)" ] && exit

echo
echo "NOTICE: SSH (22/tcp) is the only inbound service enabled by default."
echo

mkdir -p /etc/iptables.d/{filter,nat,mangle}/{INPUT,OUTPUT}
mkdir -p /etc/iptables.d/{filter,mangle}/FORWARD
mkdir -p /etc/iptables.d/{nat,mangle}/{PRE,POST}ROUTING
mkdir -p /etc/iptables.d/filter/{BLACKLIST_CHECK,FORWARD_DROP,VALIDATE_TCP_DROP,VALIDATE_TCP,DROPLOG,INPUT_DROP,OVERLIMIT_DROP,OUTPUT_LOG_ALLOW,OUTPUT_DROP,THROTTLED_DROP}

ln -s /usr/share/fwtree/rules/nat/_GLOBAL /etc/iptables.d/nat/
ln -s /usr/share/fwtree/rules/filter/_GLOBAL /etc/iptables.d/filter/
ln -s /usr/share/fwtree/rules/mangle/_GLOBAL /etc/iptables.d/mangle/

ln -s /usr/share/fwtree/rules/nat/_BEGIN /etc/iptables.d/nat/
ln -s /usr/share/fwtree/rules/filter/BLACKLIST_CHECK/99-blacklist-check /etc/iptables.d/filter/BLACKLIST_CHECK/
ln -s /usr/share/fwtree/rules/filter/BLACKLIST_CHECK/01-noblacklist-check /etc/iptables.d/filter/BLACKLIST_CHECK/
ln -s /usr/share/fwtree/rules/filter/FORWARD_DROP/01-drop /etc/iptables.d/filter/FORWARD_DROP/
ln -s /usr/share/fwtree/rules/filter/VALIDATE_TCP_DROP/01-drop /etc/iptables.d/filter/VALIDATE_TCP_DROP/
ln -s /usr/share/fwtree/rules/filter/INPUT/90-udp-allow-dhcp /etc/iptables.d/filter/INPUT/
ln -s /usr/share/fwtree/rules/filter/INPUT/07-icmp-allow /etc/iptables.d/filter/INPUT/
ln -s /usr/share/fwtree/rules/filter/INPUT/09-validate-network /etc/iptables.d/filter/INPUT/
ln -s /usr/share/fwtree/rules/filter/INPUT/zz99-INPUT_DROP /etc/iptables.d/filter/INPUT/
ln -s /usr/share/fwtree/rules/filter/INPUT/09-BLACKLIST_CHECK /etc/iptables.d/filter/INPUT/
ln -s /usr/share/fwtree/rules/filter/_BEGIN /etc/iptables.d/filter/
ln -s /usr/share/fwtree/rules/filter/VALIDATE_TCP/01-validate-tcp /etc/iptables.d/filter/VALIDATE_TCP/
ln -s /usr/share/fwtree/rules/filter/DROPLOG/01-drop-and-log /etc/iptables.d/filter/DROPLOG/
ln -s /usr/share/fwtree/rules/filter/OUTPUT/07-icmp-allow /etc/iptables.d/filter/OUTPUT/
ln -s /usr/share/fwtree/rules/filter/OUTPUT/zz99-OUTPUT_DROP /etc/iptables.d/filter/OUTPUT/
ln -s /usr/share/fwtree/rules/filter/OUTPUT/yy99-OUTPUT_LOG_ALLOW /etc/iptables.d/filter/OUTPUT/
ln -s /usr/share/fwtree/rules/filter/INPUT_DROP/01-drop /etc/iptables.d/filter/INPUT_DROP/
ln -s /usr/share/fwtree/rules/filter/FORWARD/07-icmp-allow /etc/iptables.d/filter/FORWARD/
ln -s /usr/share/fwtree/rules/filter/FORWARD/90-loopback /etc/iptables.d/filter/FORWARD/
ln -s /usr/share/fwtree/rules/filter/FORWARD/zz99-FORWARD_DROP /etc/iptables.d/filter/FORWARD/
ln -s /usr/share/fwtree/rules/filter/OVERLIMIT_DROP/01-drop /etc/iptables.d/filter/OVERLIMIT_DROP/
ln -s /usr/share/fwtree/rules/filter/OUTPUT_LOG_ALLOW/01-allow /etc/iptables.d/filter/OUTPUT_LOG_ALLOW/
ln -s /usr/share/fwtree/rules/filter/OUTPUT_DROP/01-drop /etc/iptables.d/filter/OUTPUT_DROP/
ln -s /usr/share/fwtree/rules/filter/THROTTLED_DROP/01-drop /etc/iptables.d/filter/THROTTLED_DROP/
ln -s /usr/share/fwtree/rules/mangle/_BEGIN /etc/iptables.d/mangle/
ln -s /usr/share/fwtree/rules/COMMENT /etc/iptables.d/

ln -s /etc/iptables.d/filter/_GLOBAL/03-VALIDATE_TCP /etc/iptables.d/filter/INPUT/
ln -s /etc/iptables.d/filter/_GLOBAL/03-VALIDATE_TCP /etc/iptables.d/filter/OUTPUT/
ln -s /etc/iptables.d/filter/_GLOBAL/03-VALIDATE_TCP /etc/iptables.d/filter/FORWARD/

ln -s /etc/iptables.d/filter/_GLOBAL/05-established /etc/iptables.d/filter/INPUT/
ln -s /etc/iptables.d/filter/_GLOBAL/05-established /etc/iptables.d/filter/OUTPUT/
ln -s /etc/iptables.d/filter/_GLOBAL/05-established /etc/iptables.d/filter/FORWARD/

ln -s /etc/iptables.d/filter/_GLOBAL/08-lo-input-allow /etc/iptables.d/filter/INPUT/

ln -s /etc/iptables.d/filter/_GLOBAL/22-tcp-allow-ssh-throttled /etc/iptables.d/filter/INPUT/

ln -s /etc/iptables.d/filter/_GLOBAL/98-tcp-allow-fin-rst /etc/iptables.d/filter/INPUT/
ln -s /etc/iptables.d/filter/_GLOBAL/98-tcp-allow-fin-rst /etc/iptables.d/filter/OUTPUT/
ln -s /etc/iptables.d/filter/_GLOBAL/98-tcp-allow-fin-rst /etc/iptables.d/filter/FORWARD/

ln -s /etc/iptables.d/mangle/_GLOBAL/10-tos-default /etc/iptables.d/mangle/PREROUTING
ln -s /etc/iptables.d/mangle/_GLOBAL/10-tos-default /etc/iptables.d/mangle/POSTROUTING
ln -s /etc/iptables.d/mangle/_GLOBAL/10-tos-default /etc/iptables.d/mangle/OUTPUT
ln -s /etc/iptables.d/mangle/_GLOBAL/10-tos-default /etc/iptables.d/mangle/FORWARD

/usr/sbin/fwtree-update-blacklists

%files
%defattr (-, root, root)
/usr/sbin/fwtree
/usr/sbin/fwtree-parser
/usr/sbin/fwtree-update-blacklists
/usr/sbin/ipset-helper
/etc/iptables.d
/etc/cron.d/fwtree
/etc/ipset.d/noblacklist-ewheelerinc
/etc/rsyslog.d/20-fwtree.conf
/usr/share/fwtree
/usr/lib/systemd/system/fwtree.service
