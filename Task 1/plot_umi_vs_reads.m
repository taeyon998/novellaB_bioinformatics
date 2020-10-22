% Plot the 2D graph, using UMI function defined in UMI.m

% Constants
MAX_UMI = 30;
ITERATION = 100;

% Gener
reads = zeros(4,1);
umi = zeros(4,1);

for i = 1 : ITERATION
    [reads(i), umi(i)] = UMI(MAX_UMI, 50*i, 0.002);
end

data = [reads, umi]

plot(reads,umi, 'rx');
axis([0, reads(ITERATION), 0, MAX_UMI * 1.5]);
xlabel('Raw reads per cell');
ylabel('UMI per cell');