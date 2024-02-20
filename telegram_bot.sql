CREATE DATABASE telegram_bot;
use telegram_bot;
CREATE TABLE language_pdf (
    language VARCHAR(50),
    pdf_path VARCHAR(255)
);
INSERT INTO language_pdf (language, pdf_path)
VALUES 
    ('python', 'https://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/Python-Projects.pdf'),
    ('c++', 'https://web.corral.tacc.utexas.edu/CompEdu/pdf/isp/EijkhoutProgrammingProjects-book.pdf'),
    ('javascript', 'https://ec.europa.eu/programmes/erasmus-plus/project-result-content/7495d79c-501a-4a4d-b487-0f76ff257a2f/Games%20Development%20in%20JavaScript.pdf'),
    ('html', 'https://ncert.nic.in/textbook/pdf/kect201.pdf'),
    ('css', 'https://www2.d125.org/applied_arts/teched/courses/WEB/wd1Files/cssProject1.pdf'),
    ('java', 'https://www.diva-portal.org/smash/get/diva2:831358/FULLTEXT01.pdf'),  
    ('php', 'https://assets.ctfassets.net/nkydfjx48olf/5qFMF3mvitLMahX67i7iOb/028229996c13cbc27a0538f055a41b46/php_cookbook.pdf'),
    ('kotlin', 'https://www.ebookfrenzy.com/pdf_previews/Kotlin30EssentialsPreview.pdf'),
    ('sql', 'https://github.com/UmaAgrawal/SQL-project-on-Retail-store/blob/master/Retail%20data%20analysis.pdf');
-- Note : Grant access to telegram bot as the query mentioned below :
--     GRANT ALL PRIVILEGES ON telegram_bot.* TO 'root'@'localhost';




