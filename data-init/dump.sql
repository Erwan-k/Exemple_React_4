 SET NAMES utf8 ;
DROP TABLE IF EXISTS `Users`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Users` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `mdp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `Token`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Token` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `token_` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `Adresse_mail_non_verif`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Adresse_mail_non_verif` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `Changer_de_mdp_code`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Changer_de_mdp_code` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


