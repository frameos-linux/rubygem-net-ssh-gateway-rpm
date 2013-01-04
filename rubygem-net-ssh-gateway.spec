# Generated from net-ssh-gateway-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname net-ssh-gateway
%define version 1.1.0
%define release 2

Summary: A simple library to assist in establishing tunneled Net::SSH connections
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://net-ssh.rubyforge.org/gateway
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: rubygem-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
Requires: rubygem-net-ssh >= 1.99.1
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(net-ssh-gateway) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A simple library to assist in establishing tunneled Net::SSH connections


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/net-ssh-gateway-1.1.0/CHANGELOG.rdoc
%doc %{gemdir}/gems/net-ssh-gateway-1.1.0/lib/net/ssh/gateway.rb
%{gemdir}/gems/net-ssh-gateway-1.1.0/Manifest
%{gemdir}/gems/net-ssh-gateway-1.1.0/Rakefile
%doc %{gemdir}/gems/net-ssh-gateway-1.1.0/README.rdoc
%{gemdir}/gems/net-ssh-gateway-1.1.0/setup.rb
%{gemdir}/gems/net-ssh-gateway-1.1.0/test/gateway_test.rb
%{gemdir}/gems/net-ssh-gateway-1.1.0/net-ssh-gateway.gemspec


%doc %{gemdir}/doc/net-ssh-gateway-1.1.0
%{gemdir}/cache/net-ssh-gateway-1.1.0.gem
%{gemdir}/specifications/net-ssh-gateway-1.1.0.gemspec

%changelog
