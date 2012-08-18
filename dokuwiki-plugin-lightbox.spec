%define		plugin		lightbox
%define		ver			2012-08-08
%define		rpmver		%(echo %{ver} | tr -d -)
Summary:	DokuWiki Lightbox plugin
Summary(pl.UTF-8):	Wtyczka lightbox dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	%{rpmver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/downloads/glensc/dokuwiki-plugin-lightboxv2/lightbox-%{ver}.zip
# Source0-md5:	3bb365f181fe18520154f8debb9931d4
URL:		http://www.dokuwiki.org/plugin:lightboxv2
BuildRequires:	unzip
Requires:	dokuwiki >= 20111110
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Plugin to integrate Lightbox JavaScript animation in DokuWiki.

%prep
%setup -qc
mv %{plugin}/* .

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ $(echo "$version" | tr -d -) != %{version} ]; then
	: %%{version} mismatch, should be: $(echo "$version" | tr -d -)
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/images
