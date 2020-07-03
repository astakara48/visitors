server_name *.compute.amazonaws.com;

location / {
  uwsgi_pass unix:///home/ubuntu/visitors/tmp/visitors.sock;
  include uwsgi_params;
}

location /static/ {
  alias /home/ubuntu/visitors/staticfiles/;
}