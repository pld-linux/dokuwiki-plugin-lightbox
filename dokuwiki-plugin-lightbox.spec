%define		plugin		lightbox
Summary:	DokuWiki Light Box v2 plugin
Summary(pl.UTF-8):	Wtyczka lightboxv2 dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20090312
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.lokeshdhakar.com/projects/lightbox2/releases/lightbox2.04.zip
# Source0-md5:	c930f97a5791f202d7c48303de36f282
Patch0:		%{name}.patch
Patch1:		%{name}-konqueror.patch
Patch2:		%{name}-dw-jscompress.patch
URL:		http://wiki.splitbrain.org/plugin:lightboxv2
BuildRequires:	js
BuildRequires:	sharutils
BuildRequires:	shrinksafe
Requires:	dokuwiki >= 20090214-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Plugin to integrate LightBox v2 javascript animation in DokuWiki.

%prep
%setup -qc -n %{plugin}
%patch0 -p1
%patch1 -p1
%patch2 -p1
(
	cat js/prototype.js
	cat js/effects.js
	cat js/builder.js
	cat js/lightbox.js
) > script.js
uudecode blank.gif.uue
chmod a+r images/blank.gif
chmod a-x css/lightbox.css

rm -f images/bullet.gif
rm -f images/donate-button.gif
rm -f images/download-icon.gif
rm -f images/image-1.jpg
rm -f images/thumb-1.jpg

cat <<'EOF' > AUTHORS
ogeidix <diegogiorgini#gmail.com>
 - the original plugin

Laurent Beneytout <laurent.beneytout#gmail.com>
 - made plugin work by remaking the plugin

Elan Ruusamäe <glen#pld-linux.org>
 - made plugin work with konqueror
 - made plugin work with compression enabled
EOF
awk -vv=%{version} 'BEGIN{printf("%s-%s-%s\n", substr(v, 1, 4), substr(v, 5, 2), substr(v, 7, 2))}' > VERSION

%build
js_compress() {
	for a in "$@"; do
		# compress
		shrinksafe -c script.js > $a.tmp && mv $a.tmp script.js
		# trim newlines
		tr -d '\r\n' < script.js > $a.tmp && mv $a.tmp script.js
		# check syntax
		js -C -f script.js
	done
}
js_compress script.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a images script.js $RPM_BUILD_ROOT%{plugindir}
cp -a css/lightbox.css $RPM_BUILD_ROOT%{plugindir}/screen.css
cp -a AUTHORS VERSION $RPM_BUILD_ROOT%{plugindir}

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
%{plugindir}/images
