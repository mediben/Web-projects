-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Lun 27 Octobre 2014 à 00:09
-- Version du serveur :  5.0.27-community-nt
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `benads`
--

-- --------------------------------------------------------

--
-- Structure de la table `ads`
--

CREATE TABLE IF NOT EXISTS `ads` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `price` int(11) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `picture` varchar(255) NOT NULL,
  `categories_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Contenu de la table `ads`
--

INSERT INTO `ads` (`id`, `title`, `description`, `price`, `mail`, `picture`, `categories_id`) VALUES
(1, 'Beautiful Dobermann', 'Had 1st & 2nd Vaccines, All Black & Tan.\r\nDad is Brown & Tan.. Mum is Black & Tan both Great with my kids loving & well behaved.\r\ncome with a Bag of Royal Canin Puppy Food which is what they have been raised on.. Plus a Toy & blanket that smells like home..\r\nIf you are interested Only call.', 752, 'louis.test@mail.com', 'doberman.jpg', 2),
(2, 'Cat', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. ', 147, 'email@email.com', 'cat.jpg', 2),
(3, 'Ipad air', 'Ipad black 16G, all functionality', 340, 'me.owner@mail.com', 'myphone.jpg', 6),
(4, 'Lumia 520', 'Best Phone ever, windows and cool  Azure cloud.Nice', 200, 'fun@mail.fr', 'lumia.jpg', 6),
(5, 'Front-End  Developper ', 'Skills : Mysql,HTML5, PHP5 etc...\r\n', 3500, 'company@mail.com', 'logoa.jpg', 1),
(6, 'Summer Home', 'For rent a beuatiful summer home, located in the north of the city.\r\none week only', 150, 'steve@mailme.dk', 'myhome.jpg', 5),
(7, 'appartment', 'For rent a big appartment,two bedroom , WC and one big room\r\none month only', 640, 'gilly@mymail.com', 'home.jpg', 5),
(8, 'Hummer Limo', 'One of its kind , a black limo', 40000, 'stevie@mailme.com', 'limo.jpg', 3),
(9, 'Horse', 'Lorem gidthun lorem gidthun Lorem gidthun Lorem gidthun Lorem gidthun Lorem gidthun Lorem gidthun Lorem gidthun Lorem gidthun ', 1540, 'mailhorse@mail.com', 'horse.jpg', 2),
(10, 'Canari', 'Lovely canari lorem burem lirim lorem burem lirim lorem burem lirim lorem burem lirim lorem burem lirim', 40, 'canari@mail.fr', 'canari.jpg', 2),
(11, 'Call Centre', 'Lorem buily ruilm Loremy buil ruilm Lorem buil ruilm Lorem buil ruilym Lorem buil ruilm Lorem buil ruilm Lorem buil ruilmy', 200, 'companyall@mail.fr', 'callcentre.jpg', 4);

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE IF NOT EXISTS `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `picture` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Contenu de la table `categories`
--

INSERT INTO `categories` (`id`, `title`, `picture`) VALUES
(1, 'Jobs', 'jobs.png'),
(2, 'Pets', 'pets.png'),
(3, 'Cars', 'cars.png'),
(4, 'Services', 'services.png'),
(5, 'Rents', 'rent.png'),
(6, 'Technologies', 'technologies.png');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
