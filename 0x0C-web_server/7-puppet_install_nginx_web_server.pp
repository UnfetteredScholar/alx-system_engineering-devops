# Installs and configures nginx

package { 'nginx':
  ensure => 'installed'
}

file { 'index.html':
  path    => '/var/www/html/',
  content => 'Hello World!',
}

file { 'error-page.html':
  path    => '/var/www/html/',
  content => "Ceci n'est pas une page\n",
}

file { 'default':
  path    => '/etc/nginx/sites-enabled',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /error-page.html;
        location  /error-page.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;
        }
}
"
}


