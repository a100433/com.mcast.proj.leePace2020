pkg install -forge io
pkg load io
c = csv2cell('geo.csv');
c(1,:) % will print all headers
c(2:end,:) % will all  data rows

clear ; close all; clc

% Load CSV files
X = csvread('geo.csv');

% Split labels from pixels
y = X(:,1);
X = X(:,[1 2]:end);

% Changes 0 to 10 in label vector (useful for Prof. Ng script)
y = y + (y == 0) * 10;

% Spliting 30k for training and 12k for validation
Xval = X(30001:end,:);
yval = y(30001:end);
X = X(1:30000,:);
y = y(1:30000);

% Saving to a binary zipped mat file
save -mat7-binary -zip geo.mat X y Xval yval;