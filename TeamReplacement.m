
skills_stat = csvread('E:\study materials\SML\project\Team replacement\skill_matrix_replacement.csv');
num_skills = size(skills_stat, 2);
skills = cell(num_skills, 1);
team = 'Leicester City';
year = '2015 - 2016';

for i = 1:num_skills
    col = skills_stat(:,i);
    avg = mean(col);
    deviation = std(col);
    col = col - avg;
    col = col/deviation;
    skills{i} = diag(skills_stat(:, i)'); 
end

players = size(skills_stat, 1);
adjacency = csvread('E:\study materials\SML\project\Team replacement\coordination_matrix_replacement.csv');

currentTeam = [12 6 13 1 24 15 14 4 17 10 16];
memberToReplace = currentTeam(5);
%Reference to implementation of Random Walk Graph Kernel in "https://github.com/jackiey99/WWW2015_code"
%Reference paper "Replacing the Irreplaceable: Fast Algorithm for Team Member Recommendation"
score = GraphSimilarity(adjacency, skills, currentTeam, memberToReplace, 'false'); 
disp(score);