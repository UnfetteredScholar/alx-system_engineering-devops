# Installs and configures nginx

package { 'nginx':
  ensure => 'installed'
}

file { 'index.html':
  path => '/var/www/html/',
  content => 'Hello World!',
}

file { 'error-page.html':
  path => '/var/www/html/',
  content => "Ceci n'est pas une page\n",
}

$server_config = @("CONFIG")
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }
        error_page 404 /error-page.html;
        location = /error-page.html {
                internal;
        }
        if ($request_filename ~ redirect_me){
                rewrite ^ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;
        }
}
| CONFIG	

file { 'default':
  path => '/etc/nginx/sites-enabled',
  content => $server_config
}


