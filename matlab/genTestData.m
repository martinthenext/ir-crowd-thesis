% Include subdirectories to use GPML code
addpath(genpath('./'))

% Generate data
n1 = 80; n2 = 40;
S1 = eye(2); S2 = [1 0.95; 0.95 1];
m1 = [0.75; 0]; m2 = [-0.75; 0];
x1 = bsxfun(@plus, chol(S1)'*gpml_randn(0.2, 2, n1), m1);
x2 = bsxfun(@plus, chol(S2)'*gpml_randn(0.3, 2, n2), m2);

x = [x1 x2]'; 
y = [-ones(1,n1) ones(1,n2)]';

% Test data
[t1 t2] = meshgrid(-4:0.1:4,-4:0.1:4);
t = [t1(:) t2(:)]; 
n = length(t);

% Saving
save('train.mat', 'x', 'y');
save('test.mat', 't');
