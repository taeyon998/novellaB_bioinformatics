% input: P = num copies of each UMI, capRate = probability of capture, possible_umis = total number of UMIs in cell
% output: umi_count = num of UMIs detected in reads
function [read_count, umi_count] = UMI(possible_UMIs, P, capRate)

% 1. [10 UMIs] generate 40k arr, 4k of 0-9 each 
% Eg. arr = [zeros(4000,1); ones(4000,1); 2*ones(4000,1); 3*ones(4000,1); 4*ones(4000,1); 5*ones(4000,1); 6*ones(4000,1); 7*ones(4000,1); 8*ones(4000,1); 9*ones(4000,1)];
arr = zeros(P,1);
for i = 2 : possible_UMIs
    arr = [arr; (i-1) * ones(P, 1)];
end

% 2. [0.2% seq -> N reads] randomly select 80 data sets
%Eg. all_perm = randperm(40000);
all_perm = randperm(length(arr));

reads = zeros(1,capRate * length(arr));

for i = 1 : capRate * length(arr)
    reads(i) = arr(all_perm(i)); %1xR array of sequenced reads
end

%Number of UMIs
count = 1;
umi = reads(1);

for i = 2 : length(reads)
    % check for new UMI
    new_umi = 1;
    
    for k = 1 : length(umi)
        % if same umi is found
        if umi(k) == reads(i)
            new_umi = 0;
            break;
        end   
    end
    %if new UMI, store it & increment count
    if(new_umi)
        umi(count+1) = reads(i);
        count = count + 1;
    end
end
umi_count = count;
read_count = length(reads);

end
