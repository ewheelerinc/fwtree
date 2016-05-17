Name: fwtree
Summary: Tree-driven firewall
Version: 1.0.1
Release: 2.el7
BuildArch: noarch
Group: Application
License: Restricted
Prefix: /
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ipset
Conflicts: firewalld
AutoReqProv: no

%description

%build
cp /usr/src/fwtree-git/base/-1.0.1-2.el7.noarch.tar %{_builddir}/-1.0.1-2.el7.noarch.tar

%install
mkdir -p $RPM_BUILD_ROOT/
mv -1.0.1-2.el7.noarch.tar $RPM_BUILD_ROOT/-1.0.1-2.el7.noarch.tar
cd $RPM_BUILD_ROOT/
tar -xf $RPM_BUILD_ROOT/-1.0.1-2.el7.noarch.tar
rm $RPM_BUILD_ROOT/-1.0.1-2.el7.noarch.tar

%clean
rm -fr $RPM_BUILD_ROOT

%post
test -e /etc/iptables.d/COMMENT && exit

echo "Warning: SSH is the only service allowed by default."

ln -s /usr/share/fwtree/rules/COMMENT /etc/iptables.d/
ln -s /usr/share/fwtree/rules/nat/_GLOBAL /etc/iptables.d/nat/
ln -s /usr/share/fwtree/rules/filter/_GLOBAL /etc/iptables.d/filter/
ln -s /usr/share/fwtree/rules/mangle/_GLOBAL /etc/iptables.d/mangle/

ln -s /usr/share/fwtree/rules/filter/DROPLOG/01-drop-and-log /etc/iptables.d/filter/DROPLOG/
ln -s /usr/share/fwtree/rules/filter/OUTPUT_DROP_ALLOW/01-allow /etc/iptables.d/filter/OUTPUT_DROP_ALLOW/

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

%files
%defattr (-, root, root)
/usr/sbin/fwtree
/usr/sbin/fwtree-parser
/usr/sbin/fwtree-update-blacklists
/usr/sbin/ipset-helper
/etc/iptables.d
/usr/share/fwtree
/usr/lib/systemd/system/fwtree.service
