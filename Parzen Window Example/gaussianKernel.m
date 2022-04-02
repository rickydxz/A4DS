function K = gaussianKernel(X1, X2, spread)
% This code is for educational and research purposes of comparisons. 
% Credit will be given to the referenced developer and Emanuel Parzen.
%
% This function evaluates the Gaussian on the input data and 
% returns the kernal values. In (Parzen,1962) the kernal function are 
% defined as the weighting functions.   
% 
% Reference:
%    [1] Parzen, E., On the Estimation of a Probability Density Function 
%        and Mode, 1962
%    [2] Duin, R.P.W and Pekalska, E., Pattern Recognition Tools, 
%        http://37steps.com/37-steps/

[row1,col1]=size(X1); % Testing Data
[row2,col2]=size(X2); % Training Data
N = row2;
D = col2;
K = zeros(row1,row2);
for i = 1:row1
    for j = 1:row2
        % The ... in Matlab is a continuation of the code
        K(i,j) = (1/((sqrt(2*pi)*spread))^D)*...
            exp(-0.5*(((X1(i,:)-X2(j,:))*(X1(i,:)-X2(j,:))')/(spread^2)));
    end
end